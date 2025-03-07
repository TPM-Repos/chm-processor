Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentFactoryAttribute Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ComponentFactoryAttribute Class](topic6167.md) : ComponentFactoryAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentFactoryType_
    The factory class responsible for creating components.

Glossary Item Box

Initializes a new instance of the [ComponentFactoryAttribute](topic6167.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _componentFactoryType_ As Type _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim componentFactoryType As Type
     
    Dim instance As New [ComponentFactoryAttribute](topic6167.md)(componentFactoryType)  
  
C#|   
---|---  
      
    
    public ComponentFactoryAttribute( 
       Type _componentFactoryType_
    )  
  
#### Parameters

 _componentFactoryType_
    The factory class responsible for creating components.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentFactoryAttribute Class](topic6167.md)   
[ComponentFactoryAttribute Members](topic6168.md)


