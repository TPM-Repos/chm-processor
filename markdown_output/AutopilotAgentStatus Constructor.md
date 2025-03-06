![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AutopilotAgentStatus Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2420.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AutopilotAgentStatus Class](topic2414.md) : AutopilotAgentStatus Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_agentName_
    

_isRunning_
    

_isStarting_
    

_isStopping_
    

_emailQueueEnabled_
    

_triggerQueueEnabled_
    

_specificationQueueEnabled_
    

_previewQueueEnabled_
    

_modelGenQueueEnabled_
    

Glossary Item Box

Creates a new instance of the [AutopilotAgentStatus](topic2414.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _agentName_ As String, _
       ByVal _isRunning_ As Boolean, _
       ByVal _isStarting_ As Boolean, _
       ByVal _isStopping_ As Boolean, _
       ByVal _emailQueueEnabled_ As Boolean, _
       ByVal _triggerQueueEnabled_ As Boolean, _
       ByVal _specificationQueueEnabled_ As Boolean, _
       ByVal _previewQueueEnabled_ As Boolean, _
       ByVal _modelGenQueueEnabled_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim agentName As String
    Dim isRunning As Boolean
    Dim isStarting As Boolean
    Dim isStopping As Boolean
    Dim emailQueueEnabled As Boolean
    Dim triggerQueueEnabled As Boolean
    Dim specificationQueueEnabled As Boolean
    Dim previewQueueEnabled As Boolean
    Dim modelGenQueueEnabled As Boolean
     
    Dim instance As New [AutopilotAgentStatus](topic2414.md)(agentName, isRunning, isStarting, isStopping, emailQueueEnabled, triggerQueueEnabled, specificationQueueEnabled, previewQueueEnabled, modelGenQueueEnabled)  
  
C#|   
---|---  
      
    
    public AutopilotAgentStatus( 
       string _agentName_ ,
       bool _isRunning_ ,
       bool _isStarting_ ,
       bool _isStopping_ ,
       bool _emailQueueEnabled_ ,
       bool _triggerQueueEnabled_ ,
       bool _specificationQueueEnabled_ ,
       bool _previewQueueEnabled_ ,
       bool _modelGenQueueEnabled_
    )  
  
#### Parameters

 _agentName_
    
_isRunning_
    
_isStarting_
    
_isStopping_
    
_emailQueueEnabled_
    
_triggerQueueEnabled_
    
_specificationQueueEnabled_
    
_previewQueueEnabled_
    
_modelGenQueueEnabled_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AutopilotAgentStatus Class](topic2414.md)   
[AutopilotAgentStatus Members](topic2415.md)

©2024 DriveWorks Ltd. All Rights Reserved.
