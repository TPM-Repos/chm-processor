Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewResultInvalidated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IPreviewDocument Interface](topic2263.md) : PreviewResultInvalidated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the preview result becomes out of date. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event PreviewResultInvalidated As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewDocument](topic2263.md)
    Dim handler As EventHandler
     
    AddHandler instance.PreviewResultInvalidated, handler  
  
C#|   
---|---  
      
    
    event EventHandler PreviewResultInvalidated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewDocument Interface](topic2263.md)   
[IPreviewDocument Members](topic2264.md)


