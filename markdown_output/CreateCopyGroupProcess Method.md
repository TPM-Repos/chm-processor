![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateCopyGroupProcess Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9783.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupProcess Class](topic9776.md) : CreateCopyGroupProcess Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceGroup_
    The source group.

_targetGroup_
    The target group.

_options_
    The options to use.

Glossary Item Box

Creates a new instance of the [CopyGroupProcess](topic9776.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function CreateCopyGroupProcess( _
       ByVal _sourceGroup_ As [Group](topic2958.md), _
       ByVal _targetGroup_ As [Group](topic2958.md), _
       ByVal _options_ As [CopyGroupOptions](topic9736.md) _
    ) As [CopyGroupProcess](topic9776.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim sourceGroup As [Group](topic2958.md)
    Dim targetGroup As [Group](topic2958.md)
    Dim options As [CopyGroupOptions](topic9736.md)
    Dim value As [CopyGroupProcess](topic9776.md)
     
    value = [CopyGroupProcess](topic9776.md).CreateCopyGroupProcess(sourceGroup, targetGroup, options)  
  
C#|   
---|---  
      
    
    public static [CopyGroupProcess](topic9776.md) CreateCopyGroupProcess( 
       [Group](topic2958.md) _sourceGroup_ ,
       [Group](topic2958.md) _targetGroup_ ,
       [CopyGroupOptions](topic9736.md) _options_
    )  
  
#### Parameters

 _sourceGroup_
    The source group.
_targetGroup_
    The target group.
_options_
    The options to use.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CopyGroupProcess Class](topic9776.md)   
[CopyGroupProcess Members](topic9777.md)

©2024 DriveWorks Ltd. All Rights Reserved.
