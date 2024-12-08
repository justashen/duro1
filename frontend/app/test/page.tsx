/* eslint-disable padding-line-between-statements */
"use client";
/* eslint-disable react/jsx-sort-props */
/* eslint-disable prettier/prettier */

import React, { useState, ChangeEvent, FormEvent } from "react";
import { FaWhatsapp } from "react-icons/fa";
import {
  CircleUser,
  Tags,
  Globe,
  FileText,
  SkipForward,
  CheckCircle,
} from "lucide-react";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Input } from "@nextui-org/input";
import { Button } from "@nextui-org/button";

type FormData = {
  projectName: string;
  metaTitle: string;
  metaDescription?: string;
  whatsappNumber: string;
  domain?: string;
};

type Errors = {
  projectName?: string;
  metaTitle?: string;
  whatsappNumber?: string;
};

type StepProps = {
  icon: React.ReactNode;
  name: string;
  placeholder: string;
  value: string | undefined;
  error?: string;
  onChange: (e: ChangeEvent<HTMLInputElement>) => void;
};

const StepInput: React.FC<StepProps> = ({
  icon,
  name,
  placeholder,
  value,
  error,
  onChange,
}) => (
  <div>
    <div className="flex items-center">
      {icon}
      <Input
        name={name}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        aria-label={name}
      />
    </div>
    {error && <p className="text-red-500 text-sm mt-1">{error}</p>}
  </div>
);

const NavigationButtons: React.FC<{
  onPrevious?: () => void;
  onSkip?: () => void;
  onNext?: () => void;
  onSubmit?: () => void;
  isLastStep?: boolean;
}> = ({ onPrevious, onSkip, onNext, onSubmit, isLastStep }) => (
  <div className="flex justify-between mt-4">
    {onPrevious && (
      <Button onClick={onPrevious} variant="ghost">
        Previous
      </Button>
    )}
    {onSkip && (
      <Button onClick={onSkip} variant="faded" className="mr-2">
        <SkipForward className="mr-2 h-4 w-4" /> Skip
      </Button>
    )}
    {isLastStep ? (
      <Button onClick={onSubmit} type="button">
        Complete Setup
      </Button>
    ) : (
      <Button onClick={onNext} type="button">
        Next
      </Button>
    )}
  </div>
);

const ProjectSetupForm = () => {
  const [step, setStep] = useState<number>(1);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);
  const [formData, setFormData] = useState<FormData>({
    projectName: "",
    metaTitle: "",
    whatsappNumber: "",
  });
  const [errors, setErrors] = useState<Errors>({});

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const validateStep = (): boolean => {
    const newErrors: Errors = {};

    if (step === 1 && !formData.projectName) {
      newErrors.projectName = "Project name is required";
    } else if (
      step === 2 &&
      (!formData.metaTitle || formData.metaTitle.length < 10)
    ) {
      newErrors.metaTitle = "Meta title must be between 10-60 characters";
    } else if (step === 4) {
      if (!formData.whatsappNumber) {
        newErrors.whatsappNumber = "WhatsApp number is required";
      } else {
        const whatsappRegex = /^\+(\d{1,4})\d{6,15}$/;
        if (!whatsappRegex.test(formData.whatsappNumber)) {
          newErrors.whatsappNumber =
            "Please enter a valid WhatsApp number with a country code (e.g., +94773795678)";
        }
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleNext = () => {
    if (validateStep()) setStep((prev) => prev + 1);
  };

  const handleSkip = () => {
    setErrors({});
    setStep((prev) => prev + 1);
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (validateStep()) {
      console.log(
        "FULL PROJECT SUBMISSION:",
        JSON.stringify(formData, null, 2)
      );
      setIsSubmitted(true);
    }
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
              {formData.metaDescription && (
                <p>
                  <strong>Meta Description:</strong> {formData.metaDescription}
                </p>
              )}
              <p>
                <strong>WhatsApp Number:</strong> {formData.whatsappNumber}
              </p>
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

  const steps = [
    {
      icon: <CircleUser className="mr-2 h-4 w-4 text-gray-400" />,
      name: "projectName",
      placeholder: "Project Name (Internal Reference)",
    },
    {
      icon: <Tags className="mr-2 h-4 w-4 text-gray-400" />,
      name: "metaTitle",
      placeholder: "Your website's title",
    },
    {
      icon: <FileText className="mr-2 h-4 w-4 text-gray-400" />,
      name: "metaDescription",
      placeholder: "Say about your shop in 2 sentences",
    },
    {
      icon: <FaWhatsapp className="mr-2 h-4 w-4 text-gray-400" />,
      name: "whatsappNumber",
      placeholder: "Your WhatsApp number eg:+94773795678",
    },
    {
      icon: <Globe className="mr-2 h-4 w-4 text-gray-400" />,
      name: "domain",
      placeholder: "Domain Name (You can connect later)",
    },
  ];

  const currentStep = steps[step - 1];
  const titles: string[] = [
    "Name Your Project",
    "Provide a Title for Your Web Page",
    "Add a Description",
    "Add your WhatsApp Number",
    "Connect Your Domain",
  ];

  return (
    <div className="flex justify-center items-center min-h-screen light:bg-gray-100 dark:bg-[#0f0f0f] p-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <h2 className="text-center w-full">
            Step {step} - {titles[step - 1]}
          </h2>
        </CardHeader>
        <CardBody>
          <form>
            <StepInput
              icon={currentStep.icon}
              name={currentStep.name}
              placeholder={currentStep.placeholder}
              value={formData[currentStep.name as keyof FormData]}
              onChange={handleChange}
              error={errors[currentStep.name as keyof Errors]}
            />
            <NavigationButtons
              onPrevious={step > 1 ? () => setStep(step - 1) : undefined}
              onNext={step < steps.length ? handleNext : undefined}
              onSkip={
                [3, 5].includes(step) ? handleSkip : undefined
              }
              // @ts-ignore //TODO:
              onSubmit={step === steps.length ? handleSubmit : undefined}
              isLastStep={step === steps.length}
            />
          </form>
        </CardBody>
      </Card>
    </div>
  );
};

export default ProjectSetupForm;
