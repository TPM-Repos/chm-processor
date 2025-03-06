       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VerifyingGenerationRequired Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IGenerationService Interface](topic15147.md) : VerifyingGenerationRequired Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised before DriveWorks checks to determine whether generation of the current component is required. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event VerifyingGenerationRequired As EventHandler(Of VerifyingGenerationRequiredEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGenerationService](topic15147.md)
    Dim handler As EventHandler(Of VerifyingGenerationRequiredEventArgs)
     
    AddHandler instance.VerifyingGenerationRequired, handler  
  
C#|   
---|---  
      
    
    event EventHandler<VerifyingGenerationRequiredEventArgs> VerifyingGenerationRequired  
  
# Event Data

The event handler receives an argument of type [VerifyingGenerationRequiredEventArgs](topic13917.md) containing data related to this event. The following **VerifyingGenerationRequiredEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ComponentDetails](topic13923.md)| Gets the details of the component currently being evaluated.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGenerationService Interface](topic15147.md)   
[IGenerationService Members](topic15148.md)


