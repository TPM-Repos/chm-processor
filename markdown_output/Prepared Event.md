Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Prepared Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IDrawingGenerationContext Interface](topic15135.md) : Prepared Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when preparation of the drawing for generation has completed successfully. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Prepared As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDrawingGenerationContext](topic15135.md)
    Dim handler As EventHandler
     
    AddHandler instance.Prepared, handler  
  
C#|   
---|---  
      
    
    event EventHandler Prepared  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDrawingGenerationContext Interface](topic15135.md)   
[IDrawingGenerationContext Members](topic15136.md)


