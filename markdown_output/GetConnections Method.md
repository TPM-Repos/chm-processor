Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConnections Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutput Class](topic7074.md) : GetConnections Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all connections that has been made to this output. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetConnections() As IEnumerable(Of Connection)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NodeOutput](topic7074.md)
    Dim value As IEnumerable(Of Connection)
     
    value = instance.GetConnections()  
  
C#|   
---|---  
      
    
    public IEnumerable<Connection> GetConnections()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NodeOutput Class](topic7074.md)   
[NodeOutput Members](topic7075.md)


