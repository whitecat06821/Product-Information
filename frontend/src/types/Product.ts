export interface Product {
  title: string;
  description: string;
  tags: string[];
  colors?: string[]; // Made optional as it might not always be present or returned by the model
} 