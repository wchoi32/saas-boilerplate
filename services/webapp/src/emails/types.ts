import { ComponentType } from 'react';

export enum EmailTemplateType {
  AccountActivation = 'accountActivation',
}

export interface EmailComponentProps {
  to: string;
  webAppUrl: string;
}

export interface EmailTemplateDefinition {
  Template: ComponentType<any>;
  Subject: ComponentType<any>;
}