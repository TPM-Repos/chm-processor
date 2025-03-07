Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Find Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : Find Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSetName_
    The name of the component set to find.

Glossary Item Box

Finds a component set with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Find( _
       ByVal _componentSetName_ As String _
    ) As [ProjectComponentSet](topic4106.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
    Dim componentSetName As String
    Dim value As [ProjectComponentSet](topic4106.md)
     
    value = instance.Find(componentSetName)  
  
C#|   
---|---  
      
    
    public [ProjectComponentSet](topic4106.md) Find( 
       string _componentSetName_
    )  
  
#### Parameters

 _componentSetName_
    The name of the component set to find.

#### Return Value

A component set, or a null reference if no match is found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)


