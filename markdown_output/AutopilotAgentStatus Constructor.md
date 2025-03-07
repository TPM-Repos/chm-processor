Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AutopilotAgentStatus Constructor   
  
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

# Syntax

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
  
Visual Basic (Usage)| Copy Code  
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
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AutopilotAgentStatus Class](topic2414.md)   
[AutopilotAgentStatus Members](topic2415.md)


