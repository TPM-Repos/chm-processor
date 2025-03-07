Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopiedMasterModel Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IModelGenerationContext Interface](topic15157.md) : CopiedMasterModel Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the master model has been copied to the target location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event CopiedMasterModel As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IModelGenerationContext](topic15157.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.CopiedMasterModel, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> CopiedMasterModel  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IModelGenerationContext Interface](topic15157.md)   
[IModelGenerationContext Members](topic15158.md)


