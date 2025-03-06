       

_T_
    

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetService<T> Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : SetService<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_service_
    

Glossary Item Box

Sets a service on the Project. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetService(Of T)( _
       ByVal _service_ As T _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim service As T
     
    instance.SetService(Of T)(service)  
  
C#|   
---|---  
      
    
    public void SetService<T>( 
       T _service_
    )  
  
#### Parameters

 _service_
    

#### Type Parameters

_T_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


