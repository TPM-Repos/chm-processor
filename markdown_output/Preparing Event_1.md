Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Preparing Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IModelGenerationContext Interface](topic15157.md) : Preparing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the component is being prepared for generation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Preparing As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IModelGenerationContext](topic15157.md)
    Dim handler As EventHandler
     
    AddHandler instance.Preparing, handler  
  
C#|   
---|---  
      
    
    event EventHandler Preparing  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IModelGenerationContext Interface](topic15157.md)   
[IModelGenerationContext Members](topic15158.md)


