/* eslint-disable padding-line-between-statements */
"use client";
/* eslint-disable react/jsx-sort-props */
/* eslint-disable prettier/prettier */
import React, { useState, ChangeEvent, FormEvent } from "react";
import {
  CircleUser,
  Tags,
  Globe,
  FileText,
  MapPin,
  SkipForward,
  CheckCircle,
} from "lucide-react";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Input } from "@nextui-org/input";
import { Button } from "@nextui-org/button";

type FormData = {
  projectName: string;
  metaTitle: string;
  physicalAddress?: string;
  metaDescription?: string;
  domain?: string;
};

type Errors = {
  projectName?: string;
  metaTitle?: string;
};

const ProjectSetupForm: React.FC = () => {
  const [step, setStep] = useState<number>(1);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);
  const [formData, setFormData] = useState<FormData>({
    projectName: "",
    metaTitle: "",
  });
  const [errors, setErrors] = useState<Errors>({});

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const validateProjectName = (): boolean => {
    const newErrors: Errors = {};
    if (!formData.projectName) {
      newErrors.projectName = "Project name is required";
    } else if (formData.projectName.length < 2) {
      newErrors.projectName = "Project name must be at least 2 characters";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const validateMetaTitle = (): boolean => {
    const newErrors: Errors = {};
    if (!formData.metaTitle) {
      newErrors.metaTitle = "Meta title is required";
    } else if (
      formData.metaTitle.length < 10 ||
      formData.metaTitle.length > 60
    ) {
      newErrors.metaTitle = "Meta title must be between 10-60 characters";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleNext = () => {
    if (step === 1 && validateProjectName()) {
      setStep(2);
    } else if (step === 2 && validateMetaTitle()) {
      setStep(3);
    }
  };

  const handleSkip = () => {
    setStep((prevStep) => prevStep + 1);
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (!formData.projectName || !formData.metaTitle) {
      alert("Please fill in the required fields (Project Name and Meta Title)");
      return;
    }
    console.log("FULL PROJECT SUBMISSION:", JSON.stringify(formData, null, 2));
    setIsSubmitted(true);
  };

  if (isSubmitted) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-green-50 p-4">
        <Card className="w-full max-w-md text-center">
          <CardBody className="p-8">
            <CheckCircle className="mx-auto mb-4 h-16 w-16 text-green-600" />
            <h2 className="text-2xl font-bold mb-4">Setup Complete!</h2>
            <p className="mb-4">Your project has been successfully set up.</p>
            <div className="bg-green-100 p-4 rounded-lg text-left">
              <h3 className="font-semibold mb-2">Project Details:</h3>
              <p>
                <strong>Project Name:</strong> {formData.projectName}
              </p>
              <p>
                <strong>Meta Title:</strong> {formData.metaTitle}
              </p>
              {formData.physicalAddress && (
                <p>
                  <strong>Address:</strong> {formData.physicalAddress}
                </p>
              )}
              {formData.metaDescription && (
                <p>
                  <strong>Meta Description:</strong> {formData.metaDescription}
                </p>
              )}
              {formData.domain && (
                <p>
                  <strong>Domain:</strong> {formData.domain}
                </p>
              )}
            </div>
          </CardBody>
        </Card>
      </div>
    );
  }

  const renderStep = () => {
    switch (step) {
      case 1:
        return (
          <div>
            <div className="flex items-center">
              <CircleUser className="mr-2 h-4 w-4 text-gray-400" />
              <Input
                name="projectName"
                placeholder="Project Name (Internal Reference)"
                value={formData.projectName}
                onChange={handleChange}
                aria-label="Project Name"
              />
            </div>
            {errors.projectName && (
              <p className="text-red-500 text-sm mt-1">{errors.projectName}</p>
            )}
            <Button onClick={handleNext} className="w-full mt-4" type="button">
              Next
            </Button>
          </div>
        );
      case 2:
        return (
          <div>
            <div className="flex items-center">
              <Tags className="mr-2 h-4 w-4 text-gray-400" />
              <Input
                name="metaTitle"
                placeholder="Meta Title (For Search Engines)"
                value={formData.metaTitle}
                onChange={handleChange}
                aria-label="Meta Title"
              />
            </div>
            {errors.metaTitle && (
              <p className="text-red-500 text-sm mt-1">{errors.metaTitle}</p>
            )}
            <div className="flex justify-between mt-4">
              <Button onClick={() => setStep(1)} variant="ghost">
                Previous
              </Button>
              <Button onClick={handleNext} type="button">
                Next
              </Button>
            </div>
          </div>
        );
      case 3:
        return (
          <div>
            <div className="flex items-center">
              <MapPin className="mr-2 h-4 w-4 text-gray-400" />
              <Input
                name="physicalAddress"
                placeholder="Physical Address (Optional)"
                value={formData.physicalAddress}
                onChange={handleChange}
                aria-label="Physical Address"
              />
            </div>
            <div className="flex justify-between mt-4">
              <Button onClick={() => setStep(2)} variant="ghost">
                Previous
              </Button>
              <Button onClick={handleSkip} variant="faded" className="mr-2">
                <SkipForward className="mr-2 h-4 w-4" /> Skip
              </Button>
              <Button onClick={handleNext} type="button">
                Next
              </Button>
            </div>
          </div>
        );
      case 4:
        return (
          <div>
            <div className="flex items-center">
              <FileText className="mr-2 h-4 w-4 text-gray-400" />
              <Input
                name="metaDescription"
                placeholder="Meta Description (Optional)"
                value={formData.metaDescription}
                onChange={handleChange}
                aria-label="Meta Description"
              />
            </div>
            <div className="flex justify-between mt-4">
              <Button onClick={() => setStep(3)} variant="ghost">
                Previous
              </Button>
              <Button onClick={handleSkip} variant="faded" className="mr-2">
                <SkipForward className="mr-2 h-4 w-4" /> Skip
              </Button>
              <Button onClick={handleNext} type="button">
                Next
              </Button>
            </div>
          </div>
        );
      case 5:
        return (
          <div>
            <div className="flex items-center">
              <Globe className="mr-2 h-4 w-4 text-gray-400" />
              <Input
                name="domain"
                placeholder="Domain Name (Optional)"
                value={formData.domain}
                onChange={handleChange}
                aria-label="Domain"
              />
            </div>
            <div className="flex justify-between mt-4">
              <Button onClick={() => setStep(4)} variant="ghost">
                Previous
              </Button>
              <Button onClick={handleSkip} variant="faded" className="mr-2">
                <SkipForward className="mr-2 h-4 w-4" /> Skip
              </Button>
              <Button onClick={handleSubmit} type="button">
                Complete Setup
              </Button>
            </div>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen light:bg-gray-100 dark:bg-[#0f0f0f] p-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <h2 className="text-center">
            Project Setup - Step {step}
          </h2>
        </CardHeader>
        <CardBody>
          <form>{renderStep()}</form>
        </CardBody>
      </Card>
    </div>
  );
};

export default ProjectSetupForm;

