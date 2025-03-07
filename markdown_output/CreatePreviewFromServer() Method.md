Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatePreviewFromServer() Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) > [CreatePreviewFromServer Method](topic8716.md) : CreatePreviewFromServer() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates a preview from the server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreatePreviewFromServer() As [PreviewResult](topic8817.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim value As [PreviewResult](topic8817.md)
     
    value = instance.CreatePreviewFromServer()  
  
C#|   
---|---  
      
    
    public [PreviewResult](topic8817.md) CreatePreviewFromServer()  
  
# Remarks

This is a synchronous operation and so previews will be processed one at a time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)   
[Overload List](topic8716.md)


