Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ModelGenerationContextCreated Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IGenerationService Interface](topic15147.md) : ModelGenerationContextCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a model generation context is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ModelGenerationContextCreated As EventHandler(Of ModelGenerationContextEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGenerationService](topic15147.md)
    Dim handler As EventHandler(Of ModelGenerationContextEventArgs)
     
    AddHandler instance.ModelGenerationContextCreated, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ModelGenerationContextEventArgs> ModelGenerationContextCreated  
  
# Event Data

The event handler receives an argument of type [ModelGenerationContextEventArgs](topic15264.md) containing data related to this event. The following **ModelGenerationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic15271.md)| Gets the generation context.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGenerationService Interface](topic15147.md)   
[IGenerationService Members](topic15148.md)


