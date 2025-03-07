_TService_
    The type of service to request.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetService<TService>() Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) > [GetService Method](topic3878.md) : GetService<TService>() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a service from the project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetService(Of TService)() As TService  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim value As TService
     
    value = instance.GetService(Of TService)()  
  
C#|   
---|---  
      
    
    public TService GetService<TService>()  
  
#### Type Parameters

_TService_
    The type of service to request.

#### Return Value

A service of the requested type, or a null reference if not found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)   
[Overload List](topic3878.md)


