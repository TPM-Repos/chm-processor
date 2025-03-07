Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Prepared Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IModelGenerationContext Interface](topic15157.md) : Prepared Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when preparation of the component for generation has completed successfully. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Prepared As EventHandler(Of ModelPreparationResultEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IModelGenerationContext](topic15157.md)
    Dim handler As EventHandler(Of ModelPreparationResultEventArgs)
     
    AddHandler instance.Prepared, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ModelPreparationResultEventArgs> Prepared  
  
# Event Data

The event handler receives an argument of type [ModelPreparationResultEventArgs](topic15272.md) containing data related to this event. The following **ModelPreparationResultEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[PreviouslyFailed](topic15279.md)| Gets whether, while preparing the model, it was determined that an attempt to generate the model on a previous occasion had failed.   
[Result](topic15280.md)| Gets the model preparation result.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IModelGenerationContext Interface](topic15157.md)   
[IModelGenerationContext Members](topic15158.md)


