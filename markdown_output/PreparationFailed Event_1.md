Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreparationFailed Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IModelGenerationContext Interface](topic15157.md) : PreparationFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an exception occurs during the preparation of the component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PreparationFailed As EventHandler(Of ExceptionEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IModelGenerationContext](topic15157.md)
    Dim handler As EventHandler(Of ExceptionEventArgs)
     
    AddHandler instance.PreparationFailed, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ExceptionEventArgs> PreparationFailed  
  
# Event Data

The event handler receives an argument of type [ExceptionEventArgs](topic806.md) containing data related to this event. The following **ExceptionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Exception](topic813.md)| Gets the exception to which the event refers.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IModelGenerationContext Interface](topic15157.md)   
[IModelGenerationContext Members](topic15158.md)


