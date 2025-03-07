Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConnectionEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ConnectionEventArgs Class](topic6930.md) : ConnectionEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connection_
    The [Connection](topic6909.md) for the event.

Glossary Item Box

Creates a new instance of the [ConnectionEventArgs](topic6930.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _connection_ As [Connection](topic6909.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim connection As [Connection](topic6909.md)
     
    Dim instance As New [ConnectionEventArgs](topic6930.md)(connection)  
  
C#|   
---|---  
      
    
    public ConnectionEventArgs( 
       [Connection](topic6909.md) _connection_
    )  
  
#### Parameters

 _connection_
    The [Connection](topic6909.md) for the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionEventArgs Class](topic6930.md)   
[ConnectionEventArgs Members](topic6931.md)


