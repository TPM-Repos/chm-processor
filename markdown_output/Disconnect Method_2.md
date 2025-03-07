Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Disconnect Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeNavigationInput Class](topic7058.md) : Disconnect Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_connection_
    The connection to remove.

Glossary Item Box

Removes the given connection from this input. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Disconnect( _
       ByVal _connection_ As [Connection](topic6909.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeNavigationInput](topic7058.md)
    Dim connection As [Connection](topic6909.md)
    Dim value As Boolean
     
    value = instance.Disconnect(connection)  
  
C#|   
---|---  
      
    
    public bool Disconnect( 
       [Connection](topic6909.md) _connection_
    )  
  
#### Parameters

 _connection_
    The connection to remove.

#### Return Value

True if the connection was removed, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeNavigationInput Class](topic7058.md)   
[NodeNavigationInput Members](topic7059.md)


