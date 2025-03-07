Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewInvalidated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) : PreviewInvalidated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever the result of [GetPreview](topic8723.md) has changed significantly. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event PreviewInvalidated As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.PreviewInvalidated, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<EventArgs> PreviewInvalidated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)


