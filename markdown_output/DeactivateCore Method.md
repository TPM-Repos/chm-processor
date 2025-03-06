![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeactivateCore Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1128.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : DeactivateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_cancel_
    The view should set this value to true before exiting the method if the view wishes to cancel the view switch.

Glossary Item Box

When overridden by a derived class, performs deactivation logic specific to the derived view. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub DeactivateCore( _
       ByRef _cancel_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim cancel As Boolean
     
    instance.DeactivateCore(cancel)  
  
C#|   
---|---  
      
    
    protected virtual void DeactivateCore( 
       ref bool _cancel_
    )  
  
#### Parameters

 _cancel_
    The view should set this value to true before exiting the method if the view wishes to cancel the view switch.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
