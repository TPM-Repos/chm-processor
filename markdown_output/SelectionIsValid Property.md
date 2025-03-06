![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SelectionIsValid Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8331.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ListControlBase Class](topic8315.md) : SelectionIsValid Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a value indicating whether the current selection is valid. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property SelectionIsValid As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ListControlBase](topic8315.md)
    Dim value As Boolean
     
    value = instance.SelectionIsValid  
  
C#|   
---|---  
      
    
    public bool SelectionIsValid {get;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This should always be true because we automatically update the selected item to be the first available item when the available items invalidate the current selection.

The one circumstance in which this property can return false, is when a rule has been built for the selected item, and is returning a value which is not in the list. In this case, the UI should pick-up on this property and warn the user what is going on. Additionally, when the validation routine runs, it will trace the condition to the implementation debugging log.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ListControlBase Class](topic8315.md)   
[ListControlBase Members](topic8316.md)

©2024 DriveWorks Ltd. All Rights Reserved.
