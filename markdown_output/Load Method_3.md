Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryInfo Interface](topic2055.md) : Load Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_throwOnError_
    True to allow exceptions to be thrown when loading the library.

Glossary Item Box

Loads the library if it hasn't already been loaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Load( _
       ByVal _throwOnError_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryInfo](topic2055.md)
    Dim throwOnError As Boolean
     
    instance.Load(throwOnError)  
  
C#|   
---|---  
      
    
    void Load( 
       bool _throwOnError_
    )  
  
#### Parameters

 _throwOnError_
    True to allow exceptions to be thrown when loading the library.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryInfo Interface](topic2055.md)   
[ILibraryInfo Members](topic2056.md)


