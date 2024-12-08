// /app/shop/[slug]/page.tsx
"use client";

import { useParams } from "next/navigation";

const ProductPage = () => {
  const { slug } = useParams(); // Capture the slug from the URL

  // Simulate fetching product data based on the slug (replace with actual API calls)
  const products = [
    { slug: "product-1", name: "Product 1", description: "This is product 1." },
    { slug: "product-2", name: "Product 2", description: "This is product 2." },
    { slug: "product-3", name: "Product 3", description: "This is product 3." },
  ];

  // Find the product matching the slug
  const product = products.find((p) => p.slug === slug);

  if (!product) {
    return <p>Product not found!</p>;
  }

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
    </div>
  );
};

export default ProductPage;
