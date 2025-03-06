![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActivateCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingsPage Class](topic935.md) : ActivateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_firstShow_
    True if it is the first time the page has been shown.

_cancel_
    Set to true by the overridden method to cancel the navigation action if desired.

Glossary Item Box

When overridden by a derived class, performs activation logic specific to the derived page. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub ActivateCore( _
       ByVal _firstShow_ As Boolean, _
       ByRef _cancel_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SettingsPage](topic935.md)
    Dim firstShow As Boolean
    Dim cancel As Boolean
     
    instance.ActivateCore(firstShow, cancel)  
  
C#|   
---|---  
      
    
    protected virtual void ActivateCore( 
       bool _firstShow_ ,
       ref bool _cancel_
    )  
  
#### Parameters

 _firstShow_
    True if it is the first time the page has been shown.
_cancel_
    Set to true by the overridden method to cancel the navigation action if desired.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SettingsPage Class](topic935.md)   
[SettingsPage Members](topic936.md)


