Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PostCloseStarting Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ICommonGenerationContext Interface](topic15096.md) : PostCloseStarting Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the Post Close sequence execution starts. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PostCloseStarting As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommonGenerationContext](topic15096.md)
    Dim handler As EventHandler
     
    AddHandler instance.PostCloseStarting, handler  
  
C#|   
---|---  
      
    
    event EventHandler PostCloseStarting  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommonGenerationContext Interface](topic15096.md)   
[ICommonGenerationContext Members](topic15097.md)


