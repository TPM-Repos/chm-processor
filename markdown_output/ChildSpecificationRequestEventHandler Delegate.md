![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChildSpecificationRequestEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) : ChildSpecificationRequestEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The sender of the event.

_e_
    Data for the request.

Glossary Item Box

Raised when there is a request to show a child specification dialog. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ChildSpecificationRequestEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [ChildSpecificationRequestEventArgs](topic7596.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As New [ChildSpecificationRequestEventHandler](topic9365.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ChildSpecificationRequestEventHandler( 
       object _sender_ ,
       [ChildSpecificationRequestEventArgs](topic7596.md) _e_
    )  
  
#### Parameters

 _sender_
    The sender of the event.
_e_
    Data for the request.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ChildSpecificationRequestEventHandler Members](topic9365.md)   
[DriveWorks.Forms Namespace](topic7266.md)


