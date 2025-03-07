Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LoadComponent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSet Class](topic4106.md) : LoadComponent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Loads the component from the component file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function LoadComponent() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSet](topic4106.md)
    Dim value As Boolean
     
    value = instance.LoadComponent()  
  
C#|   
---|---  
      
    
    public bool LoadComponent()  
  
#### Return Value

False if the component could not be loaded because the underlying capture data has been removed, i.e. the component has been uncaptured.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| No implementation of the component type was registered.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSet Class](topic4106.md)   
[ProjectComponentSet Members](topic4107.md)


