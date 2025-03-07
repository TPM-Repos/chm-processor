_T_
    The type of service object to get

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetService<T> Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IServiceManager Interface](topic435.md) : GetService<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the service object of the specified type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetService(Of T)() As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IServiceManager](topic435.md)
    Dim value As T
     
    value = instance.GetService(Of T)()  
  
C#|   
---|---  
      
    
    T GetService<T>()  
  
#### Type Parameters

_T_
    The type of service object to get

#### Return Value

A service object of the specified type, or a null reference (Nothing in Visual Basic) if no matching service exists.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IServiceManager Interface](topic435.md)   
[IServiceManager Members](topic436.md)


