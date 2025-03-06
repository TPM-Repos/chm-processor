![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
JobRequestTagInformation Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3610.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobRequestTagInformation Class](topic3604.md) : JobRequestTagInformation Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_priorityTags_
    The tags that must be processed first. The order of the collection determines the priority.

_blockedTags_
    The tags that must be ignored.

_processPriorityOnly_
    Optional. Whether only the priority tags will be processed. False by default.

_jobTimeOut_
    Optional. The amount in minutes the agent will have to generate the component before being marked as failed.

Glossary Item Box

Creates a new instance of the [JobRequestTagInformation](topic3604.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _priorityTags_() As String, _
       ByVal _blockedTags_() As String, _
       Optional ByVal _processPriorityOnly_ As Boolean, _
       Optional ByVal _jobTimeOut_ As Integer _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim priorityTags() As String
    Dim blockedTags() As String
    Dim processPriorityOnly As Boolean
    Dim jobTimeOut As Integer
     
    Dim instance As New [JobRequestTagInformation](topic3604.md)(priorityTags, blockedTags, processPriorityOnly, jobTimeOut)  
  
C#|   
---|---  
      
    
    public JobRequestTagInformation( 
       string[] _priorityTags_ ,
       string[] _blockedTags_ ,
       bool _processPriorityOnly_ ,
       int _jobTimeOut_
    )  
  
#### Parameters

 _priorityTags_
    The tags that must be processed first. The order of the collection determines the priority.
_blockedTags_
    The tags that must be ignored.
_processPriorityOnly_
    Optional. Whether only the priority tags will be processed. False by default.
_jobTimeOut_
    Optional. The amount in minutes the agent will have to generate the component before being marked as failed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[JobRequestTagInformation Class](topic3604.md)   
[JobRequestTagInformation Members](topic3605.md)

©2024 DriveWorks Ltd. All Rights Reserved.
