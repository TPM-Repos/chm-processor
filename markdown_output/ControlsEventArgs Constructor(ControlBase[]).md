![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlsEventArgs Constructor(ControlBase[])   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlsEventArgs Class](topic7816.md) > [ControlsEventArgs Constructor](topic7822.md) : ControlsEventArgs Constructor(ControlBase[])  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controls_
    The controls that were affected by the event.

Glossary Item Box

Initializes a new instance of the [ControlsEventArgs](topic7816.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _controls_() As [ControlBase](topic7698.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim controls() As [ControlBase](topic7698.md)
     
    Dim instance As New [ControlsEventArgs](topic7816.md)(controls)  
  
C#|   
---|---  
      
    
    public ControlsEventArgs( 
       [ControlBase](topic7698.md)[] _controls_
    )  
  
#### Parameters

 _controls_
    The controls that were affected by the event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlsEventArgs Class](topic7816.md)   
[ControlsEventArgs Members](topic7817.md)   
[Overload List](topic7822.md)


