Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddEvent Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupConnectorBase<T> Class](topic1857.md) : AddEvent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of event to add.

_description_
    The body of the event entry.

_targetName_
    The target of the current body of work that this event is for.

Glossary Item Box

Adds an event into the application log. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub AddEvent( _
       ByVal _type_ As [ApplicationEventType](topic656.md), _
       ByVal _description_ As String, _
       Optional ByVal _targetName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectorBase(Of T)](topic1857.md)
    Dim type As [ApplicationEventType](topic656.md)
    Dim description As String
    Dim targetName As String
     
    instance.AddEvent(type, description, targetName)  
  
C#|   
---|---  
      
    
    protected void AddEvent( 
       [ApplicationEventType](topic656.md) _type_ ,
       string _description_ ,
       string _targetName_
    )  
  
#### Parameters

 _type_
    The type of event to add.
_description_
    The body of the event entry.
_targetName_
    The target of the current body of work that this event is for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectorBase<T> Class](topic1857.md)   
[GroupConnectorBase<T> Members](topic1858.md)


