Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseConnectionRemoved Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [InputConnectionEndpoint Class](topic7033.md) : RaiseConnectionRemoved Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connection_
    The connection that was removed.

Glossary Item Box

Raises the [ConnectionRemoved](topic7043.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseConnectionRemoved( _
       ByVal _connection_ As [Connection](topic6909.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [InputConnectionEndpoint](topic7033.md)
    Dim connection As [Connection](topic6909.md)
     
    instance.RaiseConnectionRemoved(connection)  
  
C#|   
---|---  
      
    
    protected void RaiseConnectionRemoved( 
       [Connection](topic6909.md) _connection_
    )  
  
#### Parameters

 _connection_
    The connection that was removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[InputConnectionEndpoint Class](topic7033.md)   
[InputConnectionEndpoint Members](topic7034.md)


