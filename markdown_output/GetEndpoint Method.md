Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEndpoint Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [InputEndpointRef Class](topic12893.md) : GetEndpoint Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project to retrieve the endpoint from.

Glossary Item Box

Gets the endpoint this refers to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetEndpoint( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [InputConnectionEndpoint](topic7033.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [InputEndpointRef](topic12893.md)
    Dim project As [Project](topic3859.md)
    Dim value As [InputConnectionEndpoint](topic7033.md)
     
    value = instance.GetEndpoint(project)  
  
C#|   
---|---  
      
    
    public abstract [InputConnectionEndpoint](topic7033.md) GetEndpoint( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    The project to retrieve the endpoint from.

#### Return Value

The endpoint this reference refers to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[InputEndpointRef Class](topic12893.md)   
[InputEndpointRef Members](topic12894.md)


