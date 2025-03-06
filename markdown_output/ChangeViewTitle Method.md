![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChangeViewTitle Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic583.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IViewRegistrationService Interface](topic578.md) : ChangeViewTitle Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The culture-invariant name of the view to change.

_title_
    The new title for the view.

Glossary Item Box

Changes the title of the specified view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ChangeViewTitle( _
       ByVal _name_ As String, _
       ByVal _title_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IViewRegistrationService](topic578.md)
    Dim name As String
    Dim title As String
    Dim value As Boolean
     
    value = instance.ChangeViewTitle(name, title)  
  
C#|   
---|---  
      
    
    bool ChangeViewTitle( 
       string _name_ ,
       string _title_
    )  
  
#### Parameters

 _name_
    The culture-invariant name of the view to change.
_title_
    The new title for the view.

#### Return Value

True if the title was successfully changed, otherwise false.

# ![](dotnetimages/collapse.gif)Remarks

Will be false if the view definition doesn't exist or the title is the same as the old title.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IViewRegistrationService Interface](topic578.md)   
[IViewRegistrationService Members](topic579.md)

©2024 DriveWorks Ltd. All Rights Reserved.
