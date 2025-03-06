![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlNameChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) : ControlNameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever any control is renamed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ControlNameChanged As EventHandler(Of ControlNameChangedEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim handler As EventHandler(Of ControlNameChangedEventArgs)
     
    AddHandler instance.ControlNameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ControlNameChangedEventArgs> ControlNameChanged  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [ControlNameChangedEventArgs](topic10116.md) containing data related to this event. The following **ControlNameChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Control](topic10122.md)| The instance of the control that changed.   
[NewName](topic10123.md)| The new name of the control.   
[OldName](topic10124.md)| The original name of the control   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)


