Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Preparing Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IDrawingGenerationContext Interface](topic15135.md) : Preparing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the drawing is being prepared for generation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Preparing As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDrawingGenerationContext](topic15135.md)
    Dim handler As EventHandler
     
    AddHandler instance.Preparing, handler  
  
C#|   
---|---  
      
    
    event EventHandler Preparing  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDrawingGenerationContext Interface](topic15135.md)   
[IDrawingGenerationContext Members](topic15136.md)


