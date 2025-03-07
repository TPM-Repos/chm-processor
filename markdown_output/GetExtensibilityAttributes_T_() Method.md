_T_
    The type of extensibility attribute to get.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetExtensibilityAttributes<T>() Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryInfo Interface](topic2055.md) > [GetExtensibilityAttributes Method](topic2060.md) : GetExtensibilityAttributes<T>() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the extensibility attributes of the specified type for the extension library. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetExtensibilityAttributes(Of T)() As T()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryInfo](topic2055.md)
    Dim value() As T
     
    value = instance.GetExtensibilityAttributes(Of T)()  
  
C#|   
---|---  
      
    
    T[] GetExtensibilityAttributes<T>()  
  
#### Type Parameters

_T_
    The type of extensibility attribute to get.

#### Return Value

An array of the extensibility attribute of the specified type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryInfo Interface](topic2055.md)   
[ILibraryInfo Members](topic2056.md)   
[Overload List](topic2060.md)


