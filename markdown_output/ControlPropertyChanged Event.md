![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlPropertyChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [Form Class](topic8086.md) : ControlPropertyChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a direct child's property has changed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ControlPropertyChanged As [ControlValueChangedEventHandler](topic9588.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Form](topic8086.md)
    Dim handler As [ControlValueChangedEventHandler](topic9588.md)
     
    AddHandler instance.ControlPropertyChanged, handler  
  
C#|   
---|---  
      
    
    public event [ControlValueChangedEventHandler](topic9588.md) ControlPropertyChanged  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ControlValueChangedEventArgs](topic9385.md) containing data related to this event. The following **ControlValueChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Control](topic9393.md)| Gets the control that changed.   
[EventArgument](topic9394.md)| Gets the argument describing the source of this change.   
[NewValue](topic9395.md)| Gets the value of the property as it after the change.   
[OldValue](topic9396.md)| Gets the value of the property as it was before the change.   
[Property](topic9397.md)| Gets the property that was changed.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Form Class](topic8086.md)   
[Form Members](topic8087.md)


