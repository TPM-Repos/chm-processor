Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LastLoadException Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryInfo Interface](topic2055.md) : LastLoadException Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

If an exception occurred loading the extension library, this property will retrieve the exception. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property LastLoadException As Exception  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryInfo](topic2055.md)
    Dim value As Exception
     
    value = instance.LastLoadException  
  
C#|   
---|---  
      
    
    Exception LastLoadException {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryInfo Interface](topic2055.md)   
[ILibraryInfo Members](topic2056.md)


