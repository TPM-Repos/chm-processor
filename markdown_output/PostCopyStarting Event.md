Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PostCopyStarting Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ICommonGenerationContext Interface](topic15096.md) : PostCopyStarting Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the Post Copy sequence execution starts. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PostCopyStarting As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommonGenerationContext](topic15096.md)
    Dim handler As EventHandler
     
    AddHandler instance.PostCopyStarting, handler  
  
C#|   
---|---  
      
    
    event EventHandler PostCopyStarting  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommonGenerationContext Interface](topic15096.md)   
[ICommonGenerationContext Members](topic15097.md)


