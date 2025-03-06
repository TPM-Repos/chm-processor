       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
VariableChangedEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : VariableChangedEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle the event raised when a variable is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub VariableChangedEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [VariableEventArgs](topic5874.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [VariableChangedEventHandler](topic5938.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void VariableChangedEventHandler( 
       object _sender_ ,
       [VariableEventArgs](topic5874.md) _e_
    )  
  
#### Parameters

 _sender_
    The source of the event.
_e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VariableChangedEventHandler Members](topic5938.md)   
[DriveWorks Namespace](topic2159.md)


