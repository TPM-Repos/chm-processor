Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OutputName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationOutputDef Class](topic4056.md) : OutputName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the name of the output to retrieve from the child specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property OutputName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationOutputDef](topic4056.md)
    Dim value As String
     
    instance.OutputName = value
     
    value = instance.OutputName  
  
C#|   
---|---  
      
    
    public string OutputName {get; set;}  
  
# Remarks

The output could be from one of the types specified in [ProjectChildSpecificationOutputType](topic2357.md). This value will contain its type prefix.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationOutputDef Class](topic4056.md)   
[ProjectChildSpecificationOutputDef Members](topic4057.md)


