Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DataTableEventHandler Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : DataTableEventHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The source of the event.

_e_
    The event data.

Glossary Item Box

Represents the method that will handle the event raised when a table is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub DataTableEventHandler( _
       ByVal _sender_ As Object, _
       ByVal _e_ As [DataTableEventArgs](topic2655.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [DataTableEventHandler](topic5930.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void DataTableEventHandler( 
       object _sender_ ,
       [DataTableEventArgs](topic2655.md) _e_
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

[DataTableEventHandler Members](topic5930.md)   
[DriveWorks Namespace](topic2159.md)


