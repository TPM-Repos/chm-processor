Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DrawingGenerationContextCreated Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IModelGenerationContext Interface](topic15157.md) : DrawingGenerationContextCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a drawing generation context is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event DrawingGenerationContextCreated As EventHandler(Of DrawingGenerationContextEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IModelGenerationContext](topic15157.md)
    Dim handler As EventHandler(Of DrawingGenerationContextEventArgs)
     
    AddHandler instance.DrawingGenerationContextCreated, handler  
  
C#|   
---|---  
      
    
    event EventHandler<DrawingGenerationContextEventArgs> DrawingGenerationContextCreated  
  
# Event Data

The event handler receives an argument of type [DrawingGenerationContextEventArgs](topic15180.md) containing data related to this event. The following **DrawingGenerationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic15187.md)| Gets the generation context.   
[IsDeferred](topic15188.md)| Gets whether the drawing being generated was deferred.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IModelGenerationContext Interface](topic15157.md)   
[IModelGenerationContext Members](topic15158.md)


