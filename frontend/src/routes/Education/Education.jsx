import { Link } from "react-router-dom";

const Education = () => {
  return (
    <div className="w-2/3 pt-5 px-10">
      <h2 className="text-2xl font-bold mb-5">Bias literacy</h2>
      <p className="mb-3">
        Bias literacy refers to the ability to recognize, understand, and
        address different types of biases, especially in information, data, and
        decision-making processes. It involves awareness of how biases can
        influence perceptions, judgements, and outcomes, and it equips
        individuals with skills to critically evaluate information and minimize
        the impact of bias on their reasoning.
      </p>
      <p className="mb-5">
        In media, bias literacy involves identifying how stereotypes, framing,
        and selective visibility shape public perception, often reinforcing
        societal inequalities.
      </p>
      <div className="flex gap-7 mb-5">
        <Link
          className="text-xl font-semibold border-b-2 border-b-black"
          to="#"
        >
          Depiction
        </Link>
        <Link
          className="text-xl font-semibold border-bottom border-transparent hover:border-b-black"
          to="#"
        >
          Professional roles
        </Link>
        <Link
          className="text-xl font-semibold border-bottom border-transparent hover:border-b-black"
          to="#"
        >
          Appearance
        </Link>
        <Link
          className="text-xl font-semibold border-bottom border-transparent hover:border-b-black"
          to="#"
        >
          Choice of words
        </Link>
        <Link
          className="text-xl font-semibold border-bottom border-transparent hover:border-b-black"
          to="#"
        >
          Visibility
        </Link>
        <Link
          className="text-xl font-semibold border-bottom border-transparent hover:border-b-black"
          to="#"
        >
          Comparison &amp;&nbsp;Questioning
        </Link>
      </div>
      <p>
        <strong>Depiction bias </strong>
        occurs when journalists portray individuals in a way that reinforces
        gender stereotypes, often by emphasizing traditionally "feminine" or
        "masculine" qualities. For example, female leaders may be described with
        a focus on their appearance, emotions, or personal lives, whereas male
        leaders are often depicted through their achievements, strength, or
        authority.
      </p>
      <p>
        Journalists can avoid depiction bias by ensuring descriptions focus on
        the person’s role, expertise, and actions rather than personal
        characteristics unrelated to their professional abilities. Rather than
        highlighting appearance or family roles, they can emphasize leadership
        qualities, specific achievements, or relevant experience, creating a
        balanced portrayal that respects the individual’s professional identity.
      </p>
    </div>
  );
};

export default Education;
