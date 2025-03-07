Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
JobRequestTagInformation Constructor   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _priorityTags_() As String, _
       ByVal _blockedTags_() As String, _
       Optional ByVal _processPriorityOnly_ As Boolean, _
       Optional ByVal _jobTimeOut_ As Integer _
    )  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JobRequestTagInformation Class](topic3604.md)   
[JobRequestTagInformation Members](topic3605.md)


