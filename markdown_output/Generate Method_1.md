Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Generate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) : Generate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_generateDirectory_
    The full path to the directory which generated files' paths should be created relative to.

Glossary Item Box

Generates the document within the context of the active specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Generate( _
       ByVal _generateDirectory_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim generateDirectory As String
     
    instance.Generate(generateDirectory)  
  
C#|   
---|---  
      
    
    public void Generate( 
       string _generateDirectory_
    )  
  
#### Parameters

 _generateDirectory_
    The full path to the directory which generated files' paths should be created relative to.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Thrown if the project is not part of a running specification.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)


