![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatingControlEventArgs Constructor(String,Type)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [CreatingControlEventArgs Class](topic7826.md) > [CreatingControlEventArgs Constructor](topic7832.md) : CreatingControlEventArgs Constructor(String,Type)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controlName_
    The name of the control that is being created.

_controlType_
    The type of control that is being created.

Glossary Item Box

Initializes a new instance of the [CreatingControlEventArgs](topic7826.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _controlName_ As String, _
       ByVal _controlType_ As Type _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controlName As String
    Dim controlType As Type
     
    Dim instance As New [CreatingControlEventArgs](topic7826.md)(controlName, controlType)  
  
C#|   
---|---  
      
    
    public CreatingControlEventArgs( 
       string _controlName_ ,
       Type _controlType_
    )  
  
#### Parameters

 _controlName_
    The name of the control that is being created.
_controlType_
    The type of control that is being created.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CreatingControlEventArgs Class](topic7826.md)   
[CreatingControlEventArgs Members](topic7827.md)   
[Overload List](topic7832.md)


