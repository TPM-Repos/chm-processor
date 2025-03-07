Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectComponentSetEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSetEventArgs Class](topic4125.md) : ProjectComponentSetEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSet_
    The component set that was changed.

Glossary Item Box

Initializes a new instance of the [ProjectComponentSetEventArgs](topic4125.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _componentSet_ As [ProjectComponentSet](topic4106.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim componentSet As [ProjectComponentSet](topic4106.md)
     
    Dim instance As New [ProjectComponentSetEventArgs](topic4125.md)(componentSet)  
  
C#|   
---|---  
      
    
    public ProjectComponentSetEventArgs( 
       [ProjectComponentSet](topic4106.md) _componentSet_
    )  
  
#### Parameters

 _componentSet_
    The component set that was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSetEventArgs Class](topic4125.md)   
[ProjectComponentSetEventArgs Members](topic4126.md)


