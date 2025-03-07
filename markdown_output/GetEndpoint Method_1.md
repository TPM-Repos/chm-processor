Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEndpoint Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [OutputEndpointRef Class](topic12921.md) : GetEndpoint Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project to retrieve the endpoint from.

Glossary Item Box

Retrieves the endpoint this reference refers to. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetEndpoint( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [NodeOutput](topic7074.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OutputEndpointRef](topic12921.md)
    Dim project As [Project](topic3859.md)
    Dim value As [NodeOutput](topic7074.md)
     
    value = instance.GetEndpoint(project)  
  
C#|   
---|---  
      
    
    public abstract [NodeOutput](topic7074.md) GetEndpoint( 
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

[OutputEndpointRef Class](topic12921.md)   
[OutputEndpointRef Members](topic12922.md)


