Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventFromReflection Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [EventFromReflection Class](topic799.md) : EventFromReflection Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_obj_
    The instance of the object on which the event is defined.

_eventName_
    The name of the event.

Glossary Item Box

Initializes a new instance of the [EventFromReflection](topic799.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _obj_ As Object, _
       ByVal _eventName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim obj As Object
    Dim eventName As String
     
    Dim instance As New [EventFromReflection](topic799.md)(obj, eventName)  
  
C#|   
---|---  
      
    
    public EventFromReflection( 
       object _obj_ ,
       string _eventName_
    )  
  
#### Parameters

 _obj_
    The instance of the object on which the event is defined.
_eventName_
    The name of the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EventFromReflection Class](topic799.md)   
[EventFromReflection Members](topic800.md)


